import math
import numpy as np


def angleCalcu(v1, v2):  # 角度運算(v1,v2為向量)  np.linalg.norm 調用參數直接算平方開根號， np.dot計算內積
    distance = np.linalg.norm(v1) * np.linalg.norm(v2)
    angle = int(math.degrees(math.acos(np.dot(v1, v2) / distance)))
    return angle


# 1.垂直伸展
def armStretch(lm, lhand, rhand):
    angle_list = []

    # 骨架:肩膀11、12 手肘13、14
    # 手  :手腕0 中指12
    # 先計算手肘夾角，順序先左後右
    # 口訣:左邊骨架配右手，右邊骨架配左手，左骨奇，右骨偶
    if lm[11][0] and lm[13][0] and lm[15][0]: #左肘角度
        v1 = lm[13] - lm[11]
        v2 = lm[15] - lm[13]
        angle = angleCalcu(v1, v2)
        angle_list.append(angle)

    if lm[12][0] and lm[14][0] and lm[16][0]: #右肘角度
        v1 = lm[14] - lm[12]
        v2 = lm[16] - lm[14]
        angle = angleCalcu(v1, v2)
        angle_list.append(angle)

    # 再計算手腕夾角，順序先左後右
    if lm[13][0] and lhand[0][0] and lhand[12][0]: #左腕角度
        v1 = lhand[0] - lm[13]
        v2 = lhand[12] - lhand[0]
        angle = angleCalcu(v1, v2)
        angle_list.append(angle)
    if lm[14][0] and rhand[0][0] and rhand[12][0]: #右腕角度
        v1 = rhand[0] - lm[14]
        v2 = rhand[12] - rhand[0]
        angle = angleCalcu(v1, v2)
        angle_list.append(angle)

    return angle_list


# 3.祈禱式手臂伸展
def prayPose(lm,lhand,rhand):
    angle_list = []
    # 骨架:肩膀11、12 手肘13、14
    # 手  :手腕0 中指12
    # 先計算手肘夾角，順序先左後右
    # 口訣:左邊骨架配右手，右邊骨架配左手，左骨奇，右骨偶
    if lm[11][0] and lm[13][0] and lm[15][0]: #左手肘角度
        v1 = lm[13] - lm[11]
        v2 = lm[15] - lm[13]
        angle = angleCalcu(v1, v2)
        angle_list.append(angle)

    if lm[12][0] and lm[14][0] and lm[16][0]: #右手肘角度
        v1 = lm[14] - lm[12]
        v2 = lm[16] - lm[14]
        angle = angleCalcu(v1, v2)
        angle_list.append(angle)

    # 計算手腕夾角
    if lm[13][0] and lhand[0][0] and lhand[12][0]: #左手腕角度
        v1 = lhand[0] - lm[13]
        v2 = lhand[12] - lhand[0]
        angle = angleCalcu(v1, v2)
        angle_list.append(angle)

    if lm[14][0] and rhand[0][0] and rhand[12][0]: #右手腕角度
        v1 = rhand[0] - lm[14]
        v2 = rhand[12] - rhand[0]
        angle = angleCalcu(v1, v2)
        angle_list.append(angle)

    return angle_list





# Debug用
def test(lm, lhand, rhand):
    # 左手腕角度測試
    if lm[13][0] and lhand[0][0] and lhand[12][0]:
        v1 = lhand[0] - lm[13]
        v2 = lhand[12] - lhand[0]
        angle = angleCalcu(v1, v2)
        return angle
