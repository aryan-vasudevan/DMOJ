#include <iostream>
#include <string>
#include <set>
#include <vector>

class Player {
public:
    Player(int x, int y, std::set<std::vector<int>> blocked) {
        x = x;
        y = y;
        std::vector<int> pos = {x, y};
        blocked = blocked;
    }

};

class Player {
public:
    std::vector<int> pos = {1, 2};

};

int main() {
    Player b;

    std::cout << b.pos;

    return 0;
}