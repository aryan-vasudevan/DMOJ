#include <iostream>

int main() {
    int a1, a2, a3, b1, b2, b3;
    std::cin >> a1 >> a2 >> a3 >> b1 >> b2 >> b3;
    
    int apples = 3 * a1 + 2 * a2 + a3;
    int bananas = 3 * b1 + 2 * b2 + b3;

    if (apples > bananas) {
        std::cout << "A";
    } else if (apples < bananas) {
        std::cout << "B";
    } else {
        std::cout << "T";
    }

    return 0;
}