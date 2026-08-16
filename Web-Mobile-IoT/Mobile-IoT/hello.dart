void main(){
    String name= "Panda";
    double marks=78;
    print("Hello Name: $name, Marks: $marks");
  ////////////////////////////////////////
  String age = "19";

  assert(int.parse(age) >= 18 && !(age is String), "Age must be number at least 18.");
  print("Hello Name: $name, Age: $age");

}