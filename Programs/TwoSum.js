// ================= Problem Description =================
// Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.
// Each input will have exactly one solution, and the same element cannot be used twice.
// The order of the returned indices does not matter.
// 
// ================= Input =================
// - `nums`: An array of integers.
// - `target`: An integer representing the target sum.
// 
// ================= Output =================
// - An array of two integers representing the indices of the two numbers that add up to `target`.
// 
// ================= Example =================
// Example 1:
// Input: nums = [2,7,11,15], target = 9
// Output: [0, 1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
//
// Example 2:
// Input: nums = [3,2,4], target = 6
// Output: [1, 2]
//
// Example 3:
// Input: nums = [3,3], target = 6
// Output: [0, 1]
// =========================================================


for (var i = 0; i < nums.length; i++) {
  for (var n = 1; n < nums.length; n++) {

    if (nums[i] + nums[n] == target) {
      if (nums[i] == nums[n] && nums.indexOf(nums[i]) == nums.indexOf(nums[n])) {

        let p = nums.indexOf(nums[n]) + 1

        for (var m = p; m < nums.length; m++) {

          if (nums[i] == nums[m]) {
            return [i, m]
          }

        }

      } else {
        return ([nums.indexOf(nums[i]), nums.indexOf(nums[n])])

      }

    }

  }

}