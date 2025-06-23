<script setup lang="ts">

import { ref, onMounted } from 'vue';
import TaskRow from './TaskRow.vue';

const tasks = ref([]);

onMounted(async () => {
    await fetchTasks();
});

async function fetchTasks() {
    const response = await fetch('http://localhost:8008/api/v1/tasks/');
    tasks.value = await response.json();
}
</script>

<template>
    <h1>Task list</h1>
    <template v-for="task in tasks" :key="task._id">
        <TaskRow :task="task" />
    </template>
</template>