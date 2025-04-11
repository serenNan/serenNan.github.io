#include <iostream>

// 使用typedef定义函数指针别名
typedef int(*func_ptr)(int, double);

// 使用using定义函数指针别名
using func_ptr1 = int(*)(int, double);

// 示例函数
int exampleFunc(int a, double b) {
    return a + static_cast<int>(b);
}

int main() {
    // 使用typedef定义的别名
    func_ptr fp1 = exampleFunc;
    std::cout << "typedef result: " << fp1(5, 3.14) << std::endl;

    // 使用using定义的别名
    func_ptr1 fp2 = exampleFunc;
    std::cout << "using result: " << fp2(5, 3.14) << std::endl;

    return 0;
}