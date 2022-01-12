<template>
  <div>
    <h2>{{ title }}</h2>
    <code-highlight language="javascript" :key="componentKey">
    {{ content }}
    </code-highlight>
  </div>
</template>

<script>
import CodeHighlight from "vue-code-highlight/src/CodeHighlight.vue";
import "vue-code-highlight/themes/duotone-sea.css";
import "vue-code-highlight/themes/window.css";
export default {
  name: "CodeViewer",
  props: {
    title: String,
    content: { type: String, requried: true}
  },
  data() { 
    return { 
      componentKey: 0, 
    };
  },
  components: {
    CodeHighlight,
  },
  watch: {
    content: function(){
      this.componentKey += 1;
    }
  }
  // computed : {
  //   reservedCode(){
  //     this.componentKey += 1;  
  //     this.$forceUpdate();
  //     return this.content
  //   }
  // }

};
</script>
