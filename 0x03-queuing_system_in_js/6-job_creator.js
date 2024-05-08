import kue from 'kue';

const jobObject = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
}

export const push_notification_code = kue.createQueue();

push_notification_code.on('enqueue', (id, type) => {
    console.log('Notification job created:', id);
});

const notificationJob = push_notification_code.create('Push_Notification', jobObject).save((error) => {
    if (!error) {
        console.log('Notification job created:', notificationJob.id);
    }
});

notificationJob.on('job complete', (id) => {
    console.log('Notification job completed');
});

notificationJob.on('error', (error) => {
    console.log('Notification job failed');
});

