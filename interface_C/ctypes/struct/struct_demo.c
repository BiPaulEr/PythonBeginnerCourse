typedef struct {
    int x;
    float y;
} Point;

void modify_point(Point* p) {
    p->x = 10;
    p->y = 3.14;
}