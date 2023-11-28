#include <iostream>

int main() {
    int s1, s2, s3;
    std::cin >> s1;
    std::cin >> s2;
    std::cin >> s3;

    if (s1 + s2 + s3 != 180) {
        std::cout << "Error";
    } else {
        if (s1 == s2 && s1 == s3) {
            std::cout << "Equilateral";
        } else if (s1 == s2 || s2 == s3 || s1 == s3) {
            std::cout << "Isosceles";
        } else {
            std::cout << "Scalene";
        }
    }

    return 0;
}