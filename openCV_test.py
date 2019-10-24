import cv2

src = cv2.imread("이미지_디렉토리", cv2.IMREAD_COLOR) #이미지 불러오기
img = cv2.resize(src, dsize=(0, 0), fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA) #이미지 크기 조정 0.8배

range_red = cv2.inRange(img, (100, 65, 187), (180, 170, 250)) #형광펜의 low upper 범위 설정.

red = cv2.bitwise_and(img, img, mask = range_red) #해당부분만 남기고 검은색으로..
c = red[:,:,2] != 0 #검은색이 아닌 부분 추출
red[c] = [255,255,255] #검은색이 아닌 부분 하얀색으로 변경

#화면에 보여주기
cv2.imshow("red", red)
cv2.waitKey(0)
    