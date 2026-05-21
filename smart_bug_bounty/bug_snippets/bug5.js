async function fetchUsers() {

    const response = fetch(
        "https://jsonplaceholder.typicode.com/users"
    );

    const users = response.json();

    return users;
}

function displayUsers() {

    const users = fetchUsers();

    users.forEach(user => {
        console.log(user.name);
    });
}

displayUsers();