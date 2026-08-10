#-------- PID --------------------------------------

# error = data - setpoint
# Up = Kp * error
# Ud = Kd * (error - error_old)
# Ui = Ui + Ki * error
# U = Up + Ui + Ud
#
#


#------- обработка данных и управление -------------
dX = x + w / 2
dY = y + h / 2
# K_brake - коэфицент, учитывающий временную задержку
# вычисление ошибки (отклоение от целевого значения)
#
errorY = int(dY * K_brake)
# Расчет пропорциональной составляющей
Up = Kp * errorY
# расчет дифференциальной составляющей
Ud = Kd * (errorY - errorY_old)
# расчет интегральной составляющей
Ui = Ui + Ki * errorY
# расчет скорости движения дрона по оси OY
SPEED_Y = -int(Up + Ui + Ud)
# ошибка текущая становится ошибкой предыдущей по оси OY
errorY_old = errorY
# ограничиваем скорость полета по оси OY
if abs(SPEED_Y) > 40:
    SPEED_Y = 0
fly.send_rc_control(0, 0, SPEED_Y, 0)
#
#

#----------------------------------------------------------------------------------------------
#---------- обработка данных и управление -----------------------------------------------------
dX = x + w / 2 - SET_POINT_X
dY = y + h / 2 - SET_POINT_Y
errorY = int(dY * K_brake)
errorX = int(dX * K_brake)

Uiy = Uiy + Ki * errorY
Uix = Uix + Ki * errorX

SPEED_X = -int(Kp * errorX + Kd * (errorY - errorY_old) +Uix)
SPEED_Y = -int(Kp * errorY + Kd * (errorY - errorY_old) + Uiy)

errorY_old = errorY
errorX_old = errorX

if abs(SPEED_X) > 40:
    SPEED_X = 0
if abs(SPEED_Y) > 40:
    SPEED_Y = 0

fly.send_rc_control(SPEED_X, 0, SPEED_Y, 0)
#
#

#---------------------------------------------------------------------------------------------
#---------- обработка данных и управление ----------------------------------------------------

dX = x + w / 2 - SET_POINT_X
dY = y + h / 2 - SET_POINT_Y
face_h = h

SETPOINT_H = 150

errorY = int(dY * K_brake)
errorX = int(dX * K_brake)
errorH = (face_h - SETPOINT_H)

Uiy = Uiy + Ki * errorY
Uix = Uix + Ki * errorX
Uih = Uih + Ki * errorH

SPEED_X = -int(Kp * errorX + Kd * (errorX - errorX_old) + Uix)
SPEED_Y = -int(Kp * errorY + Kd * (errorY - errorY_old) + Uiy)
SPEED_FB = -int(Kp * errorH + Kd * (errorH - errorH_old) + Uih)

errorY_old = errorY
errorX_old = errorX
errorH_old = errorH

if abs(SPEED_X) > 40:
    SPEED_X = 0

if abs(SPEED_Y) > 40:
    SPEED_Y = 0

if abs(SPEED_FB) > 40:
    SPEED_FB = 0

print(h)
print(SPEED_FB)

fly.send_rc_control(SPEED_X, SPEED_FB, SPEED_Y, 0)






























