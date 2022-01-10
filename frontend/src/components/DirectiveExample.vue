<template>
  <div>
    <h2>vue-code-highlight example</h2>
    <div v-highlight>
      <pre class="language-javascript">
        <code>
          let isPalindrome = (word) => {
          let [length, result] = [word.length, true];
          for (let i = 0; i &lt; length / 2; i++) {
          if (word[i] !== word[length - 1 - i]) result = false;
          }
          return result;
          }
          module.exports = isPalindrome;
        </code>
      </pre>
    </div>
  </div>
</template>

<script>
import Vue from 'vue';
import VueCodeHighlight from 'vue-code-highlight';
import "vue-code-highlight/themes/duotone-sea.css";
import "vue-code-highlight/themes/window.css";

Vue.use(VueCodeHighlight);

export default {
  name: "DirectiveExample"
};
</script>