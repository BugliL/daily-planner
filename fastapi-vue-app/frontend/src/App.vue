<template>
  <div id="app">
    <h1>Daily Planner</h1>
    <TaskList />
  </div>
</template>

<script setup>
import TaskList from './components/TaskList.vue';
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
