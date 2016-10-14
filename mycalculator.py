# -*- coding:utf-8 -*-

class Buffer(object):
    def __init__(self, data):
        self.data = data
        self.offset = 0
    def peek(self):
        if self.offset >= len(self.data):
            return None
        return self.data[self.offset]
    def advance(self):
        self.offset += 1

class Token(object):
    def consume(self,buffer):
        pass
    

class TokenInt(Token):
    def consume(self,buffer):
        accum =""
        while True:
            ch = buffer.peek()
            if ch is None or ch not in "0123456789":
                break
            else:
                accum += ch
                buffer.advance()
        if accum != "":
            return ("int",int(accum))
        else:
            return None

class TokenOperator(Token):
    def consume(self,buffer):
        ch = buffer.peek()
        if ch is not None and ch in "+-":
            buffer.advance()
            return("ope",ch)
        return None
            
            
class node(object):
    pass

class NodeInt(node):
    def __init__(self,value):
        self.value = value
        
class NodeBinaryOp(node):
    def __init__(self,kind):
        self.kind = kind
        self.left = None
        self.right = None



def tokenize(string):
    buffer = Buffer(string)
    tk_int = TokenInt()
    tk_op = TokenOperator()
    tokens = []

    while buffer.peek():
        token = None
        for tk in (tk_int,tk_op):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
                break
        if not token:
            raise ValueError("Error in syntax")
            
    return tokens


# 生成二叉树
def parse(tokens):
    if tokens[0][0] != "int":
        raise ValueError("Must Start with an int")
    node = NodeInt(tokens[0][1])
    nbo = None
    last = tokens[0][0]
    # 从第二个元素开始循环
    for token in tokens[1:]:
        # 如果相邻的两个token的类型相同，则错误
        if token[0] == last:
            raise ValueError("Error in syntax")
        last = token[0]
        if token[0] == "ope":
            nbo = NodeBinaryOp(token[1])
            nbo.left = node
        if token[0] == "int":
            nbo.right = NodeInt(token[1])
            node = nbo
    return node



# 使用递归的方法计算
def calculate(nbo):
    # 如果nbo的左节点是二叉树，则递归计算左节点，直到左节点不是二叉树（整数）
    if isinstance(nbo.left, NodeBinaryOp):
        leftval = calculate(nbo.left)
    else:
        leftval = nbo.left.value

    # 判断节点符号
    if nbo.kind == "-":
        return leftval - nbo.right.value
    if nbo.kind == "+":
        return leftval + nbo.right.value
    else:
        raise ValueError("Wrong operator")

def evaluate(node):
    # 先判断二叉树是否只含有一个整数，若是则输出该值
    if isinstance(node, NodeInt):
        return node.value
    else:
        return calculate(node)


# 主程序
if __name__ == '__main__':
    # 输入表达式
    input = input('Input:')
    # 将字符串拆解成list存储到tokens中，诸如tokens=[('int',4),('ope','+'),('int',6)]
    tokens = tokenize(input)
    # 根据tokens，生成二叉树存入node中
    node = parse(tokens)
    # 计算并输出
    print ('Result:'+str(evaluate(node)))
