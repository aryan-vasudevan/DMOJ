#include <iostream>
#include <string>

std::string genProng(int spacing, int size);
std::string genHandle(int size);

int main() {
    int t, s, h;
    std::cin >> t;
    std::cin >> s;
    std::cin >> h;

    int size = 2 * s + 3;

    std::string prongRow = genProng(s, size);
    std::string handleRow = genHandle(size);

    for (int i = 0; i < t; i++) {
        std::cout << prongRow << " " << "\n";
    }

    for (int i = 0; i < size; i++) {
        std::cout << "*";
    }

    std::cout << " ";

    for (int i = 0; i < h; i++) {
        std::cout << "\n" << handleRow;

        if (i != h - 1) {
            std::cout << " ";
        }
    }

    return 0;
}

std::string genProng(int spacing, int size) {
    std::string prongRow;

    for (int i = 0; i < size; i++) {
        if (i % (spacing + 1) == 0) {
            prongRow.append("*");
        } else {
            prongRow.append(" ");
        }
    }

    prongRow.append(" ");

    return prongRow;
}

std::string genHandle(int size) {
    std::string handleRow;

    for (int i = 0; i < (int)(size / 2); i++) {
        handleRow.append(" ");
    }

    handleRow.append("*");

    return handleRow;
}