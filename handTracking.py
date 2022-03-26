import cv2
import mediapipe as mp
import poseList
import numpy as np

# region 基本設定
# 相機、基本設定
camera = cv2.VideoCapture(0)
mpSolutions_holistic = mp.solutions.holistic

# 畫筆設定
mpDraw = mp.solutions.drawing_utils
LandmarkStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=2)
ConnectionStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1)

# 偵測信心值設定0.7
holistic = mpSolutions_holistic.Holistic(min_detection_confidence=0.7)
# endregion

while camera.isOpened():
    ret, img = camera.read()

    # 取得視窗寬高
    imgWidth = img.shape[1]
    imgHeight = img.shape[0]

    if ret:
        # 轉成RGB圖像並處理姿勢偵測
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result_holistic = holistic.process(imgRGB)

        # 建立Array儲存三種姿勢點的矩陣
        pose = np.zeros((33, 2))
        hand_left = np.zeros((21,2))
        hand_right = np.zeros((21,2))


        if result_holistic.pose_landmarks and result_holistic.left_hand_landmarks and result_holistic.right_hand_landmarks:
            # region 劃出所有姿勢點
            mpDraw.draw_landmarks(img, result_holistic.pose_landmarks, mpSolutions_holistic.POSE_CONNECTIONS,
                                   LandmarkStyle, ConnectionStyle)
            mpDraw.draw_landmarks(img, result_holistic.left_hand_landmarks, mpSolutions_holistic.HAND_CONNECTIONS,
                                  LandmarkStyle, ConnectionStyle)
            mpDraw.draw_landmarks(img, result_holistic.right_hand_landmarks, mpSolutions_holistic.HAND_CONNECTIONS,
                                  LandmarkStyle, ConnectionStyle)
            # endregion

            # region 儲存相關座標
            # 儲存骨架x,y 座標
            for i in range(0,33):
                pose[i][0] = int(result_holistic.pose_landmarks.landmark[i].x * imgWidth)
                pose[i][1] = int(result_holistic.pose_landmarks.landmark[i].y * imgHeight)

            #儲存左手x,y 座標
            for i in range(0,21):
                hand_left[i][0] = int(result_holistic.left_hand_landmarks.landmark[i].x * imgWidth)
                hand_left[i][1] = int(result_holistic.left_hand_landmarks.landmark[i].y * imgHeight)

            # 儲存右手x,y 座標
            for i in range(0, 21):
                hand_right[i][0] = int(result_holistic.right_hand_landmarks.landmark[i].x * imgWidth)
                hand_right[i][1] = int(result_holistic.right_hand_landmarks.landmark[i].y * imgHeight)
            # endregion

            # region Debug用
            # Debug標記骨架或手的點
            # for i in range(0,21):
            #     cv2.putText(img,str(i),(int(hand_left[i][0]+5),int(hand_left[i][1]+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
            # for i in range(0,33):
            #     cv2.putText(img,str(i),(int(pose[i][0]+5),int(pose[i][1]+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
            #
            # # 四個角度顯示
            j = 1
            angle_list = poseList.armStretch(pose,hand_left,hand_right)
            for angle in angle_list: #依序左肘、右肘、左腕、右腕
                cv2.putText(img,str(angle), (50,100*j),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
                j+=1
            # endregion

            # region 動作評判 第0、1個元素是左右肘角度，第2、3元素是左右手腕角度
            #祈禱式: score[0] in range(110,135) and score[1] in range(110,135) \
                     # and score[2] in range(75,105) and score[3] in range(75,105)
            #垂直伸展:score[0] in range(0,15) and score[1] in range(0,15) \
                    # and score[2] in range(60,90) and score[3] in range(60,90):
            score = poseList.armStretch(pose, hand_left, hand_right) #手動選擇姿勢
            if score[0] in range(0,15) and score[1] in range(0,15) \
                    and score[2] in range(60,90) and score[3] in range(60,90):
                cv2.putText(img,"Great", (50,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
            else:
                cv2.putText(img,"Bad", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            # endregion

        # 輸出畫面
        cv2.imshow('Image', img)

    if cv2.waitKey(1) == ord('q'):
        break
