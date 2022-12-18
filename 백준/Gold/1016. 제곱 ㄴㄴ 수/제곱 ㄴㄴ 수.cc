#include <stdio.h>
#include <math.h>

int range[1000001] = { 0, };
int pow_num[1000001] = { 0, };

int main() {
	long long min, max, k;
	long long i = 0, cnt = 0;
	scanf("%lld %lld", &min, &max);
	double sq = sqrt(max);

	for (i = 2; i <= sq;) {
		if (pow_num[i] == 0) pow_num[i] = 2;
		for (int j = 2; i * j <= sq; j++) {
			pow_num[i * j] = 1;
		}
		while (pow_num[i] != 0) i++;
	}
	i = 2;
	while (i <= sq) {
		long long pow = i * i;
		long long div = ceil((double)min / pow);
		
		k = div;
		while (max >= pow * k) {
			long long index = (pow * k) - min;
			if (range[index] == 0) {
				range[index] = 1;
				cnt++;
			}
			k++;
		}
		do {
			i++;
			if (i == 1000001) break;
		} while (pow_num[i] != 2);
	}
	printf("%d", max - min - cnt + 1);


	return 0;
}