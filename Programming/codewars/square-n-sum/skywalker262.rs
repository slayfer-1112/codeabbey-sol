fn square_sum(vec: Vec<i32>) -> i32 {
  vec.iter().fold(0, |t,i| t + i*i)
}
