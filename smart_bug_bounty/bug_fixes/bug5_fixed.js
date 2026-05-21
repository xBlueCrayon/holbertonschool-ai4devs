async function fetchUsers() {

    const response = await fetch(
        "https://jsonplaceholder.typicode.com/users"
    );

    const users = await response.json();

    return users;
}

async function displayUsers() {

    const users = await fetchUsers();

    users.forEach(user => {
        console.log(user.name);
    });
}

displayUsers();