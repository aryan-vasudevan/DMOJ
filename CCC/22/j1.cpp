#include <iostream>

int main() {
    int r, s;
    std::cin >> r >> s;
    
    int c = r * 8 + s * 3;

    if (c < 28) {
        std::cout << 28;
    } else {
        std::cout << c - 28;
    }
    
    return 0;
}