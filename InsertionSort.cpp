
#include<iostream>

using namespace std;

// ���� ���� �Լ� ����
void insertionSort(int arr[], int size);

// ���� �Լ�
int main() {
	int myArr[7] = { 7, 2, 5, 1, 9, 11, 4 };
	insertionSort(myArr, 7);
	for (int i = 0; i < 7; ++i)
		cout << myArr[i] << "  ";
	return 0;
}

void insertionSort(int arr[], int size) {
	int idx = 1;
	// idx�� 1���� �����Ѵ�.
	// size�� 7���� ���� �� ���� while���� �ݺ��Ѵ�.
	while (idx < size) {
		// i�� 0���� (idx - 1)���� �ݺ��ϸ鼭 ���� ���Ѵ�.
		for (int i = 0; i < idx; ++i) {
			// ���� i��° ���Ұ� �� �ϰ� �־��� idx��° ���Һ��� ũ�ٸ�
			if (arr[i] > arr[idx]) {
				// temp�� ó�� �񱳸� �����ߴ� idx���� ���Ҹ� �������ְ�
				int temp = arr[idx];
				// idx���� i���� 1�� �ٿ����鼭 ���� �ڷ� ��ĭ�� �̷��ش�.
				for (int j = idx - 1; j >= i; --j) {
					arr[j + 1] = arr[j];
				}
				// i��° �濡 temp�� �־��ش�.
				arr[i] = temp;
				break;
			}
		}

		++idx;
	}

}