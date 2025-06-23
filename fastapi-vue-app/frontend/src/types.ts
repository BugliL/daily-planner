
enum Priority {
    HIGH = "HIGH",
    IMPORTANT = "IMPORTANT",
    LOW = "LOW"
}


interface Task {
    _id: string;
    title: string;
    completed: boolean;
    priority: Priority;
}