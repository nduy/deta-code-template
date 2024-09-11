@file:JvmName("JDoodle")
/*
 * Delta- code template
 */
 val HEIGH = 20

fun main() {
    println("Hello, world!!!")
    for (i in 0..HEIGH step 1) {
    println("Hello, world!!!")
     for (j in 0..(HEIGH-i) step 1)
    print(" ");
     for (k in  0..(2 * i + 1) step 1)
   { print("*");
   }
    /**
   for (j in 0 to (10-i) )
    print(" ");
   for (k in  0 to (2 * i + 1))
   { print("*");
    println();
    }}*/
}           
}