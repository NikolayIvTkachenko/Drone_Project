import cv2

#--------------------------------------------------------------------
if dArea > 1000:
    xc = int(dM10 / dArea)
    yc = int(dM01 / dArea)

    centroid(thresh, xc, yc)

    go_center = 330 < xc < 630 and 210 < yc < 510

    go_up = 330 < xc < 630 and 100 < yc < 210
    go_down = 330 < xc < 630 and 510 < yc < 620

    go_left = 100 < xc < 330 and 210 < yc < 510
    go_right = 620 < xc < 860 and 210 < yc < 510

    if go_center:
        velocity_reset()
        cv2.putText(thresh, "Center", (650, 50), work_font, 1, white, 2)
    elif go_up:
        fly.up_down_velocity = 30
        cv2.putText(thresh, "Up", (650, 50), work_font, 1, white, 2)
    elif go_down:
        fly.up_down_velocity = -30
        cv2.putText(thresh, "Down", (650, 50), work_font, 1, white, 2)
    elif go_left:
        fly.left_right_velocity = 20
        cv2.putText(thresh, "Left", (650, 50), work_font, 1, white, 2)
    elif go_right:
        fly.left_right_velocity = -20
        cv2.putText(thresh, "Right", (650, 50), work_font, 1, white, 2)
    else:
        velocity_reset()

else:
    velocity_reset()

#--------------------------------------------------------------------

moments = cv2.moments(thresh, 1)
dM01 = moments['m01']
dM10 = moments['m10']
dArea = moments['m00']
print(dArea)

xc = int(dM10 / dArea)
yc = int(dM01 / dArea)

centroid(thresh, xc, yc)
if dArea > 5000:
    fly.for_back_velocity = -30
    cv2.putText(thresh, "Back", (650, 50), work_font, 1, white, 2)
elif 3000 < dArea < 5000:
    go_center = 330 < xc < 630 and 210 < yc < 510
    go_up = 330 < xc < 630 and 100 < yc < 210
    go_down = 330 < xc < 630 and 510 < yc < 620
    go_left = 100 < xc <330 and 210 < yc < 510
    go_right = 620 < xc < 860 and 210 < yc < 510

    if go_center:
        velocity_reset()
        cv2.putText(thresh, "Center", (650, 50), work_font, 1, white, 2)
    elif go_up:
        fly.up_down_velocity = 30
        cv2.putText(thresh, "Up", (650, 50), work_font, 1, white, 2)
    elif go_down:
        fly.up_down_velocity = -30
        cv2.putText(thresh, "Down", (650, 50), work_font, 1, white, 2)
    elif go_left:
        fly.left_right_velocity = 20
        cv2.putText(thresh, "Left", (650, 50), work_font, 1, white, 2)
    elif go_right:
        fly.left_right_velocity = -20
        cv2.putText(thresh, "Right", (650, 50), work_font, 1, white, 2)
    else:
        velocity_reset()
elif 100 < dArea < 3000:
    fly.for_back_velocity = 20
    cv2.putText(thresh, "Forward", (650, 50), work_font, 1, white, 2)
else:
    velocity_reset()

lines_net(thresh, dx, dy)
cv2.imshow("Result", thresh)



#------------------------------------------------------------------















































