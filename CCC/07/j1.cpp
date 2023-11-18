#include <iostream>

int main() {
    int b1, b2, b3;
    std::cin >> b1;
    std::cin >> b2;
    std::cin >> b3;

    if ((b3 > b1 && b1 > b2) || (b2 > b1 && b1 > b3)) {
        std::cout << b1;
    } else if ((b3 > b2 && b2 > b1) || (b1 > b2 && b2 > b3)) {
        std::cout << b2;
    } else {
        std::cout << b3;
    }

    return 0;
}