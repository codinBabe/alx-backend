import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '1234567890',
    message: 'This is the code to verify your account'
};

const job = queue.create('push_notification_code', jobData)
    .save((error) => {
        if (!error) console.log(`Notification job created: ${job.id}`)
        else console.error('Notification job failed');
    });
job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.error('Notification job failed'));
