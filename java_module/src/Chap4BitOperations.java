public class Chap4BitOperations {
	/**
	 * Consider sharpening your bit manipulation skills by writing expressions that use bitwise operators, equality checks, and Boolean operators to do the following.
	 * • Right propagate the rightmost set bit in x, e.g., turns (01010000)2 to (01011111)2-
	 * • Compute x modulo a power of two, e.g., returns 13 for 77 mod 64.
	 * • Test if x is a power of 2, i.e., evaluates to true for x = 1, 2, 4, 8, ... , false for all other values.
	 */
	public static void main(String[] args) {
		showRightPropagate(0b01010000);
		showRightPropagate(0b00000001);
		showRightPropagate(0b00010000);
		showRightPropagate(0b01111111);

		showModulo(77, 64);
		showModulo(77, 32);
		showModulo(77, 8);
		showModulo(127, 64);
		showModulo(127, 128);
		showModulo(127, 256);

		showIsPowerOf2(0);
		showIsPowerOf2(1);
		showIsPowerOf2(2);
		showIsPowerOf2(3);
		showIsPowerOf2(4);
		showIsPowerOf2(5);
		showIsPowerOf2(6);
		showIsPowerOf2(7);
		showIsPowerOf2(8);
		showIsPowerOf2(9);
		showIsPowerOf2(10);
	}

	private static void showIsPowerOf2(final int x) {
		System.out.printf("isPowerOf2 %d -> %b%n", x, isPowerOf2(x));
	}

	private static boolean isPowerOf2(final int x) {
		return (x & x - 1) == 0;
	}

	private static void showModulo(final int a, final int b) {
		System.out.printf("modulo %d %% %d -> %d%n", a, b, modulo(a, b));
	}

	private static int modulo(final int a, final int b) {
		// create mask
		int mask = b - 1;
		return a & mask;
	}

	private static void showRightPropagate(final int x) {
		System.out.printf("rightPropagate %s -> %s%n", Integer.toBinaryString(x), Integer.toBinaryString(rightPropagate(x)));
	}

	static int rightPropagate(int x) {
		// make everything after the last set bit '1'
		int y = x - 1;
		return x | y;
	}
}