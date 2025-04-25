#include <iostream>
using namespace std;

// 左值引用重载版本
// 参数t是左值引用，用于接收左值参数
// 当传入左值时，此重载版本会被调用
template <typename T> void printValue(T &t)
{
    cout << "l-value: " << t << endl;
}

// 右值引用重载版本
// 参数t是右值引用，用于接收右值参数
// 当传入右值（包括临时对象、std::move的返回值等）时，此重载版本会被调用
template <typename T> void printValue(T &&t)
{
    cout << "r-value: " << t << endl;
}

// 通用引用函数模板
// 参数v是通用引用（universal reference），可以接收任何值类型
// T&&在模板推导时的特殊规则：
// 1. 当传入右值时，T推导为具体类型，如int
// 2. 当传入左值时，T推导为左值引用类型，如int&
template <typename T> void testForward(T &&v)
{
    // v本身在函数内是左值（具名变量都是左值）
    printValue(v);  // 一定调用左值重载版本
    
    // std::move将v转换为右值引用，强制调用右值重载版本
    printValue(move(v));
    
    // std::forward根据模板参数T的类型，按照原始类型转发
    // 如果T是普通类型（非引用），forward<T>返回右值引用
    // 如果T是左值引用类型，forward<T>返回左值引用
    printValue(forward<T>(v));
    cout << endl;
}


int main()
{
    // 场景1：传入右值
    testForward(520);  // T推导为int，v类型为int&&
    
    int num = 1314;
    // 场景2：传入左值
    testForward(num);  // T推导为int&，v类型为int&
    
    // 场景3：显式指定模板参数
    testForward(forward<int>(num));      // T=int，按右值转发
    testForward(forward<int &>(num));    // T=int&，按左值转发
    testForward(forward<int &&>(num));   // T=int&&，按右值转发

    return 0;
}
