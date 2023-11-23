#include <iostream>

int main() {
    int n1, n2, n3;
    std::cin >> n1;
    std::cin >> n2;
    std::cin >> n3;

    std::cout << "The 1-3-sum is " << n1 + (n2 * 3) + n3 + 91;
    return 0;
}