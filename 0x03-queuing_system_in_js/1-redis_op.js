import redis from 'redis';


const client = redis.createClient({
    host: 'localhost',
    port: 6379
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.log('Redis client not connected to the server: ', error);
});


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (error, reply) => {
        if (error) {
            console.log(error);
        }
        redis.print(null, reply);
    });
}


function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, reply) => {
        if (error) {
            console.log(error)
        }
        console.log(reply);
    });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
