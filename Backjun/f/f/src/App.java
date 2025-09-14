    fun main() {
        val t = readln().toLong()
        val (a, b, c, d) = readln().split(" ").map { it.toLong() }

        val p1 = a * t + b
        val p2 = c * t + d

        println( if (p1 == p2) "Yes" else "No");
    }