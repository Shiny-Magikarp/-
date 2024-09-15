import torch
import torch.nn as nn
import torch.optim as optim

# 1. 创建一个简单的数据集
# 特征
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]], dtype=torch.float32)
# 标签
y = torch.tensor([[2.0], [3.0], [4.0], [5.0]], dtype=torch.float32)

# 2. 定义一个简单的线性回归模型
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # 1个输入，1个输出

    def forward(self, x):
        return self.linear(x)

# 3. 初始化模型、损失函数和优化器
model = SimpleModel()
criterion = nn.MSELoss()  # 均方误差损失
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 学习率为0.01

# 4. 训练模型
for epoch in range(100):  # 训练100个epochs
    model.train()  # 将模型设置为训练模式
    optimizer.zero_grad()  # 清空梯度

    # 前向传播
    y_pred = model(X)

    # 计算损失
    loss = criterion(y_pred, y)

    # 反向传播
    loss.backward()

    # 更新参数
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')

# 5. 测试模型
model.eval()  # 将模型设置为评估模式
with torch.no_grad():
    test_input = torch.tensor([[5.0]], dtype=torch.float32)
    predicted = model(test_input)
    print(f'预测值: {predicted.item():.4f}')