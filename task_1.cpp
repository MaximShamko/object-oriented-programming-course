#include <iostream>
using namespace std;

const int LNAME = 25;

class STUDENT
{
	char name[LNAME];
	int age;
	float grade;

public:

	char *GetName() {   // геттеры
		return name;
	}
	int GetAge() const {
		return age;
	}
	float GetGrade() const {
		return grade;
	}
	void SetName(char *valueName) {   // cеттеры
		char *pointer = name;
		while (*valueName) { // Пока не завершилось слово
			*pointer = *valueName; // Присвоить один элемент соответствующему другому
			valueName++;
			pointer++; // Переместиться к рассмотрению следующего символа
		}
		*pointer = '\0';
	}
	void SetAge(int valueAge) {
		age = valueAge;
	}
	void SetGrade(float valueGrade) {
		grade = valueGrade;
	}
	void Set(char *valueName, int valueAge, float valueGrade) {
		SetName(valueName);
		SetAge(valueAge);
		SetGrade(valueGrade);
	}
	void Show() {
		cout << "Имя: " << name << endl << "Возраст: " << age << endl << "Рейтинг: " << grade << endl;
	}

};


int main()
{
	setlocale(LC_ALL, "Russian");
	// создаем объект класса STUDENT
	STUDENT Vasiliy;

	char inputFirst[LNAME] = "Василий";
	char *inFirst = inputFirst;
	// демонстрация корректной работы методов класса STUDENT
	Vasiliy.SetName(inFirst);
	Vasiliy.SetAge(20);
	Vasiliy.SetGrade(79.90);
	Vasiliy.Show();

	char inputSecond[LNAME] = "Вася";
	char *inSecond = inputSecond;
	Vasiliy.Set(inputSecond, 20, 80.77);

	int age_of_student = Vasiliy.GetAge();
	float grade_of_student = Vasiliy.GetGrade();
	string name_of_student = Vasiliy.GetName();
	cout << name_of_student << endl;
	cout << age_of_student << endl;
	cout << grade_of_student << endl;

	return 0;