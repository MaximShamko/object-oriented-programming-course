#include <iostream>
#include <vector>


class Base {
public:
	virtual void show() = 0;
};

template <class T>
class Point2D {
public:
	Point2D(T x, T y) : x(x), y(y) {}

protected:
	T x, y;
};

template <class T>
class Z {
public:
	Z(T z) : z(z) {}

protected:
	T z;
};

template <class T>
class H {
public:
	H(T h) : h(h) {}
	
protected:
	T h;
};

template <class T>
class Point3Dh : public Point2D<T>, public Z<T>, public H<T>, public Base {
public:
	Point3Dh(T x, T y, T z, T h) : Point2D<T>(x, y), Z<T>(z), H<T>(h) {}
	void show() {
		if (this->h != 0)
			std::cout << "(" << this->x / this->h << ", " << this->y / this->h << ", " << this->z / this->h << ")" << std::endl;
		else
			std::cout << "Четвертая координата не должна равняться 0!" << std::endl;
	}
};

int main() {
	Point3Dh <int> point_1(32, 31, 56, 4);
	Point3Dh <short> point_2(2, 4, 7, 5); 
	Point3Dh <float> point_3(4.6, 3.4, 7.2, 0);
	Point3Dh <double> point_4(34.32, 57.256, 51.696, 81.777);
	Point3Dh <long> point_5(69069, 9127698, 2133188, 2215671);

	std::vector<Base*> v;
	v.push_back((Base*)&point_1);
	v.push_back((Base*)&point_2);
	v.push_back((Base*)&point_3);
	v.push_back((Base*)&point_4);
	v.push_back((Base*)&point_5);
	
	for (auto point : v) 
		point->show();
}