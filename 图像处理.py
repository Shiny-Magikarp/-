import cv2

# 读取图像
image = cv2.imread('image.png')  # 确保这个路径存在一个图像文件

# 缩小图像
scale_percent = 50  # 按照50%缩小
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

# 显示缩小的图像
cv2.imshow('Resized Image', resized_image)

# 等待用户按键
print("按 'r' 将处理图像，按 'q' 退出。")
key = cv2.waitKey(0)

if key == ord('r'):
    #在图像上绘制方框
    rec_image = cv2.rectangle(resized_image, (50, 50), (200, 200), (255, 0, 0), 2)
    cv2.imshow('Rec Image', rec_image)

    print("按 'g' 进行模糊处理，按 'q' 退出。")
    key = cv2.waitKey(0)

    if key == ord('g'):
        # 转换为灰度图像
        gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray Image', gray_image)

        # 等待用户确认
        print("按 'b' 进行模糊处理，按 'q' 退出。")
        key = cv2.waitKey(0)

        if key == ord('b'):
            # 使用高斯模糊处理
            blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
            cv2.imshow('Blurred Image', blurred_image)

            # 等待用户确认
            print("按 't' 应用阈值处理，按 'q' 退出。")
            key = cv2.waitKey(0)

            if key == ord('t'):
                # 应用阈值
                _, binary_image = cv2.threshold(blurred_image, 127, 255, cv2.THRESH_BINARY)
                cv2.imshow('Binary Image', binary_image)

                # 等待用户确认
                print("按 'c' 查找并绘制轮廓，按 'q' 退出。")
                key = cv2.waitKey(0)

                if key == ord('c'):
                    # 查找轮廓
                    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                    # 在缩小的图像上绘制轮廓
                    cv2.drawContours(resized_image, contours, -1, (0, 255, 0), 2)  # 使用绿色绘制轮廓
                    cv2.imshow('Contours', resized_image)

                    # 等待用户按键
                    print("按任意键退出。")
                    cv2.waitKey(0)
                else:
                    print("程序退出。")
            else:
                print("程序退出。")
        else:
            print("程序退出。")
    else:
        print("程序退出。")
else:
    print("程序退出。")

# 关闭所有窗口
cv2.destroyAllWindows()