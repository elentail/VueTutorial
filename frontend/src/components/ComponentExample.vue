<template>
  <div>
    <h2>vue-code-highlight example</h2>
    <code-highlight language="javascript">
        
      let isPalindrome = (word) => {

      let [length, result] = [word.length, true];
      for (let i = 0; i &lt; length / 2; i++) {
      if (word[i] !== word[length - 1 - i]) result = false;

      }
      return result;

      }
      module.exports = isPalindrome;

    </code-highlight>
  </div>
</template>

<script>
import CodeHighlight from "vue-code-highlight/src/CodeHighlight.vue";
import "vue-code-highlight/themes/duotone-sea.css";
import "vue-code-highlight/themes/window.css";
export default {
  name: "ComponentExample",
  components: {
    CodeHighlight
  }
};
</script>