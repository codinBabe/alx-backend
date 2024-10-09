import redis from 'redis';

const client = redis.createClient({
    host: 'localhost',
    port: 6379,
})

client.on('error', (error) => {
    console.error('Redis client not connected to the server:', error);
})

client.on('connect', () => {
    console.log('Redis client connected to the server')
}); 

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, value) => {
        if (error) throw error;
        console.log(value);
    });
}
displaySchoolValue('Holberton');
setNewSchool('Holberton', '98');
displaySchoolValue('Holberton');
