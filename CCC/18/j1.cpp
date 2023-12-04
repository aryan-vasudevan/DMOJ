#include <iostream>

int main() {
    int n1, n2, n3, n4;
    std::cin >> n1 >> n2 >> n3 >> n4;

    if ((n1 == 8 || n1 == 9) && (n4 == 8 || n4 == 9) && (n2 == n3)) {
        std::cout << "ignore";
    } else {
        std::cout << "answer";
    }

    return 0;
}