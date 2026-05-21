const users = [
    { name: "Alice", active: true },
    { name: "Bob", active: false },
    { name: "Charlie", active: true }
];

function getActiveUsers(userList) {

    return userList.filter(user => {

        if (user.active === true) {
            return true;
        }

        return false;
    });
}

const activeUsers = getActiveUsers(users);

console.log(activeUsers);