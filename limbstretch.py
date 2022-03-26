import cv2
import mediapipe as mp
import anglescalcu
import numpy as np

# region mediapipe 基本設定
mpSolution = mp.solutions.holistic
mpDraw = mp.solutions.drawing_utils
LandmarkStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=2)
ConnectionStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=1)
holistic = mpSolution.Holistic(min_detection_confidence=0.7)


# endregion

# 將此方法置於相機開啟的迴圈且讀得到畫面的判斷式內，並把controller的畫面變數丟入
def basic_Process(img):
    # region 取得視窗寬高、轉彩讓mp處理
    img_width = img.shape[1]
    img_height = img.shape[0]
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result_holistic = holistic.process(img_rgb)
    # endregion

    # region 建立Array儲存三種姿勢點的矩陣
    pose = np.zeros((33, 2))
    hand_left = np.zeros((21, 2))
    hand_right = np.zeros((21, 2))
    # endregion

    if result_holistic.pose_landmarks and result_holistic.left_hand_landmarks and result_holistic.right_hand_landmarks:
        # region 劃出所有姿勢點
        mpDraw.draw_landmarks(img, result_holistic.pose_landmarks, mpSolution.POSE_CONNECTIONS,
                              LandmarkStyle, ConnectionStyle)
        mpDraw.draw_landmarks(img, result_holistic.left_hand_landmarks, mpSolution.HAND_CONNECTIONS,
                                   LandmarkStyle, ConnectionStyle)
        mpDraw.draw_landmarks(img, result_holistic.right_hand_landmarks, mpSolution.HAND_CONNECTIONS,
                                   LandmarkStyle, ConnectionStyle)
        # endregion

        # region 儲存相關座標
        # 儲存骨架x,y 座標
        for i in range(0, 33):
            pose[i][0] = int(result_holistic.pose_landmarks.landmark[i].x * img_width)
            pose[i][1] = int(result_holistic.pose_landmarks.landmark[i].y * img_height)

        # 儲存左右手x,y 座標
        for i in range(0, 21):
            hand_left[i][0] = int(result_holistic.left_hand_landmarks.landmark[i].x * img_width)
            hand_left[i][1] = int(result_holistic.left_hand_landmarks.landmark[i].y * img_height)
            hand_right[i][0] = int(result_holistic.right_hand_landmarks.landmark[i].x * img_width)
            hand_right[i][1] = int(result_holistic.right_hand_landmarks.landmark[i].y * img_height)
        # endregion

        # region Debug用
        # Debug標記骨架或手的點
        # for i in range(0,21):
        #     cv2.putText(img,str(i),(int(hand_left[i][0]+5),int(hand_left[i][1]+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
        # for i in range(0,33):
        #     cv2.putText(img,str(i),(int(pose[i][0]+5),int(pose[i][1]+10)),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
        #
        # endregion

        # region 動作評判 0、1左右肘，2、3左右手腕 4、5左右膝蓋(未實作) 6、7左右腰間(未實作)
        angles = anglescalcu.all_angle(pose, hand_left, hand_right)  # 取得所有關節角度

        # region 祈禱1
        if angles[0] in range(110, 135) and angles[1] in range(110, 135) \
                and angles[2] in range(75, 105) and angles[3] in range(75, 105):
            cv2.putText(img, "Great pose:1", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # endregion

        # region 垂直伸展2
        elif angles[0] in range(0, 15) and angles[1] in range(0, 15) \
                and angles[2] in range(60, 90) and angles[3] in range(60, 90):
            cv2.putText(img, "Great pose:2", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        # endregion

        # region 雙臂平舉
        elif angles[0] in range(0, 15) and angles[1] in range(0, 15) \
                and angles[2] in range(0, 15) and angles[3] in range(0, 15):
            cv2.putText(img, "Great pose:3", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        else:
            cv2.putText(img, "Bad", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # endregion3
        # endregion

        # # region Debug 顯示角度 依序左肘、右肘、左腕、右腕
        # landmark_name = ["L-Elbow", "R-Elbow", "L-Wrist", "R-Wrist"]
        # j = 0
        # for angle in angles:
        #     cv2.putText(img, landmark_name[j] + " " + str(angle), (50, 100 * j), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
        #                 (0, 255, 0), 2)
        #     j += 1
        # # endregion

    # region 回傳結果img
    return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # endregion
