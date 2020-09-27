import cv2

cv = cv2.VideoCapture('1.mov')  # 读入视频文件，命名cv

# 输出信息
outPutInfo = {}



if cv.isOpened():  # 判断是否正常打开
  rval, frame = cv.read()
else:
  rval = False

# 获取视频帧数
VIDEO_FFRAME = cv.get(cv2.CAP_PROP_FRAME_COUNT)
outPutInfo['fframe'] = int(round(VIDEO_FFRAME))  # 四舍五入

# 获取视频宽高
VIDEO_WIDTH = cv.get(cv2.CAP_PROP_FRAME_WIDTH)
VIDEO_HEIGHT = cv.get(cv2.CAP_PROP_FRAME_HEIGHT)
outPutInfo['width'] = int(round(VIDEO_WIDTH))  # 四舍五入
outPutInfo['height'] = int(round(VIDEO_HEIGHT))  # 四舍五入

def getColorArr(colorArr):
  # 一级临时
  temp = []
  tempstr = ''
  # 组内临时
  temp2 = []
  temp2str = ''
  # 三级临时
  temp3 = ''
  # 颜色重复次数
  num = 1
  index = 1
  # 遍历行数据
  for rowrgb in colorArr:
    for rgb in rowrgb:
      print('%s/%s' % (index, len(colorArr) * len(rowrgb)))
      index += 1
      if (index > 1000):
        return temp
      for value in rgb:
        strValue = str(value)
        if (strValue != temp3):
          # 四级临时
          temp3 = strValue
          temp2str += strValue
          temp2.append(temp3)
      temp3 = ''
      if (tempstr != temp2str):
        tempstr = temp2str
        temp2.insert(0, num)
        temp.append(temp2)
        num = 1
      else:
        num += 1
      temp2str = ''
      temp2 = []
  return temp

# 打开一个文件
fo = open("output.txt", "w")
i = 0
while (rval):  # 循环读取视频帧
  rval, frame = cv.read()
  i += 1
  print(i)
  if (i == 1):
    fo.write(str(getColorArr(frame)))
    
  # cv2.imwrite('./output/{}.jpg'.format(i), frame)  # 存储为图像
  cv2.waitKey(1)

cv.release()
cv2.destroyAllWindows()
# 关闭打开的文件
fo.close()
print(outPutInfo)
