import math
import numpy as np

def angle_Calcu(v1, v2):  # 角度運算(v1,v2為向量)  np.linalg.norm 調用參數直接算平方開根號， np.dot計算內積
    distance = np.linalg.norm(v1) * np.linalg.norm(v2)
    angle = int(math.degrees(math.acos(np.dot(v1, v2) / distance)))
    return angle

# region 計算所有相關角度
def all_angle(pose,lh,rh):
    angle_list = [None] * 10
    # region 說明
    # 將長用到的關節處的角度分為:
    # 0、1 左右手肘  2、3 左右手腕    4、5 左右膝蓋(尚未實作)    6、7左右腰間(尚未實作)
    # 因鏡像畫面顯示問題，計算左邊姿態要搭配右手右腳，計算右邊姿態搭配左手左腳
    # endregion

    #region 計算左右手肘角度
    if pose[11][0] and pose[13][0] and pose[15][0]:
        v1 = pose[13] - pose[11]
        v2 = pose[15] - pose[13]
        angle_list[0] = angle_Calcu(v1, v2)

    if pose[12][0] and pose[14][0] and pose[16][0]:
        v1 = pose[14] - pose[12]
        v2 = pose[16] - pose[14]
        angle_list[1]=angle_Calcu(v1, v2)
    #endregion

    #region 計算左右手腕角度
    if pose[13][0] and lh[0][0] and lh[12][0]: #左腕角度
        v1 = lh[0] - pose[13]
        v2 = lh[12] - lh[0]
        angle_list[2] = angle_Calcu(v1, v2)
    
    if pose[14][0] and rh[0][0] and rh[12][0]: #右腕角度
        v1 = rh[0] - pose[14]
        v2 = rh[12] - rh[0]
        angle_list[3] =angle_Calcu(v1, v2)
    #endregion

    #region 計算左右膝蓋角度

    #endregion

    #region 計算左右腰間角度

    #endregion

#endregion

# region 1.垂直伸展
def arm_Stretch(pose, lh, rh):
    angle_list = []
    # 骨架:肩膀11、12 手肘13、14
    # 手  :手腕0 中指12
    # 先計算手肘夾角，順序先左後右
    # 口訣:左邊骨架配右手，右邊骨架配左手，左骨奇，右骨偶
    if pose[11][0] and pose[13][0] and pose[15][0]: #左肘角度
        v1 = pose[13] - pose[11]
        v2 = pose[15] - pose[13]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)

    if pose[12][0] and pose[14][0] and pose[16][0]: #右肘角度
        v1 = pose[14] - pose[12]
        v2 = pose[16] - pose[14]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)

    # 再計算手腕夾角，順序先左後右
    if pose[13][0] and lh[0][0] and lh[12][0]: #左腕角度
        v1 = lh[0] - pose[13]
        v2 = lh[12] - lh[0]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)
    if pose[14][0] and rh[0][0] and rh[12][0]: #右腕角度
        v1 = rh[0] - pose[14]
        v2 = rh[12] - rh[0]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)

    return angle_list
# endregion

# region 2.祈禱式手臂伸展
def pray_Pose(pose,lh,rh):
    angle_list = []
    # 骨架:肩膀11、12 手肘13、14
    # 手  :手腕0 中指12
    # 先計算手肘夾角，順序先左後右
    # 口訣:左邊骨架配右手，右邊骨架配左手，左骨奇，右骨偶
    if pose[11][0] and pose[13][0] and pose[15][0]: #左手肘角度
        v1 = pose[13] - pose[11]
        v2 = pose[15] - pose[13]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)

    if pose[12][0] and pose[14][0] and pose[16][0]: #右手肘角度
        v1 = pose[14] - pose[12]
        v2 = pose[16] - pose[14]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)

    # 計算手腕夾角
    if pose[13][0] and lh[0][0] and lh[12][0]: #左手腕角度
        v1 = lh[0] - pose[13]
        v2 = lh[12] - lh[0]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)

    if pose[14][0] and rh[0][0] and rh[12][0]: #右手腕角度
        v1 = rh[0] - pose[14]
        v2 = rh[12] - rh[0]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)

    return angle_list
#endregion

#region 3.雙臂平舉
def flat_Lift(pose,lh,rh):
    angle_list = []
    # (左~右)骨架:肩膀11、12 手肘13、14
    # (左~右)手: 手腕0 中指12
    # 先計算手肘夾角，先左後右
    if pose[11][0] and pose[13][0] and pose[15][0]: #左手肘角度
        v1 = pose[13] - pose[11]
        v2 = pose[15] - pose[13]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)

    if pose[12][0] and pose[14][0] and pose[16][0]: #右手肘角度
        v1 = pose[14] - pose[12]
        v2 = pose[16] - pose[14]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)

    # 計算手腕夾角
    if pose[13][0] and lh[0][0] and lh[12][0]: #左手腕角度
        v1 = lh[0] - pose[13]
        v2 = lh[12] - lh[0]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)

    if pose[14][0] and rh[0][0] and rh[12][0]: #右手腕角度
        v1 = rh[0] - pose[14]
        v2 = rh[12] - rh[0]
        angle = angle_Calcu(v1, v2)
        angle_list.append(angle)

    return angle_list
#endregion



# Debug用
def test(pose, lh, rh):
    # 左手腕角度測試
    if pose[13][0] and lh[0][0] and lh[12][0]:
        v1 = lh[0] - pose[13]
        v2 = lh[12] - lh[0]
        angle = angle_Calcu(v1, v2)
        return angle
