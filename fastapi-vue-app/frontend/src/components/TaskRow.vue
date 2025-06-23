<script setup lang="ts">
    const props = defineProps({
        task: {
            type: Object,
            required: false
        }
    });

    console.log('TaskRow component initialized with task:', props.task);
</script>


<template>
    <div>{{ props.task?.title }}</div>
</template>