#include <iostream>

int main() {
    int month, day;
    std::cin >> month >> day;

    if (month == 2 && day == 18) {
        std::cout << "Special";
    } else if ((month == 2 && day > 18) || month > 2) {
        std::cout << "After";
    } else {
        std::cout << "Before";
    }

    return 0;
}