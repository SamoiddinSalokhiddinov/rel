/**
 * App Calendar Events
 */

'use strict';

let date = new Date();
let nextDay = new Date(new Date().getTime() + 24 * 60 * 60 * 1000);
// prettier-ignore
let nextMonth = date.getMonth() === 11 ? new Date(date.getFullYear() + 1, 0, 1) : new Date(date.getFullYear(), date.getMonth() + 1, 1);
// prettier-ignore
let prevMonth = date.getMonth() === 11 ? new Date(date.getFullYear() - 1, 0, 1) : new Date(date.getFullYear(), date.getMonth() - 1, 1);
let events = [
      {
        id : 1,
        title: 'All Day Event',
        start: '2022-04-01',
        extendedProps: {
          calendar: 'Business'
        }
      },
      {
          id : 2,
          title: 'Meeting',
          start: '2022-04-01T10:30:00',
          end: '2022-04-01T12:30:00',
          extendedProps: {
            calendar: 'Business'
          }
      },
      {
        id : 3,
        title: 'Long Event',
        start: '2022-04-07',
        end: '2022-04-10',
        extendedProps: {
          calendar: 'Business'
        },
        slotDuration: '02:00'
      },
      {
        id : 4,
        groupId: '999',
        title: 'Repeating Event',
        start: '2022-04-08',
        end: '2022-04-11',
        extendedProps: {
          calendar: 'Business'
        }
      },
      {
        groupId: '999',
        title: 'Repeating Event',
        start: '2022-04-09',
        end: '2022-04-12',
        extendedProps: {
          calendar: 'Business'
        }
      },
    
    ]
// let events = [
//   {
//     id: 0,
//     url: '',
//     title: 'Design Review',
//     start: date,
//     end: nextDay,
//     allDay: false,
//     extendedProps: {
//       calendar: 'Business'
//     }
//   },
//   {
//     id: 1,
//     url: '',
//     title: 'Design Review',
//     start: date,
//     end: nextDay,
//     allDay: false,
//     extendedProps: {
//       calendar: 'Business'
//     }
//   },
//   {
//     id: 2,
//     url: '',
//     title: 'Meeting With Client',
//     start: new Date(date.getFullYear(), date.getMonth() + 1, -11),
//     end: new Date(date.getFullYear(), date.getMonth() + 1, -10),
//     allDay: true,
//     extendedProps: {
//       calendar: 'Business'
//     }
//   },
//   {
//     id: 3,
//     url: '',
//     title: 'Family Trip',
//     allDay: true,
//     start: new Date(date.getFullYear(), date.getMonth() + 1, -9),
//     end: new Date(date.getFullYear(), date.getMonth() + 1, -7),
//     extendedProps: {
//       calendar: 'Holiday'
//     }
//   },
//   {
//     id: 4,
//     url: '',
//     title: "Doctor's Appointment",
//     start: new Date(date.getFullYear(), date.getMonth() + 1, -11),
//     end: new Date(date.getFullYear(), date.getMonth() + 1, -10),
//     extendedProps: {
//       calendar: 'Personal'
//     }
//   },
//   {
//     id: 5,
//     url: '',
//     title: 'Dart Game?',
//     start: new Date(date.getFullYear(), date.getMonth() + 1, -13),
//     end: new Date(date.getFullYear(), date.getMonth() + 1, -12),
//     allDay: true,
//     extendedProps: {
//       calendar: 'ETC'
//     }
//   },
//   {
//     id: 6,
//     url: '',
//     title: 'Meditation',
//     start: new Date(date.getFullYear(), date.getMonth() + 1, -13),
//     end: new Date(date.getFullYear(), date.getMonth() + 1, -12),
//     allDay: true,
//     extendedProps: {
//       calendar: 'Personal'
//     }
//   },
//   {
//     id: 7,
//     url: '',
//     title: 'Dinner',
//     start: new Date(date.getFullYear(), date.getMonth() + 1, -13),
//     end: new Date(date.getFullYear(), date.getMonth() + 1, -12),
//     extendedProps: {
//       calendar: 'Family'
//     }
//   },
//   {
//     id: 8,
//     url: '',
//     title: 'Product Review',
//     start: new Date(date.getFullYear(), date.getMonth() + 1, -13),
//     end: new Date(date.getFullYear(), date.getMonth() + 1, -12),
//     allDay: true,
//     extendedProps: {
//       calendar: 'Business'
//     }
//   },
//   {
//     id: 9,
//     url: '',
//     title: 'Monthly Meeting',
//     start: nextMonth,
//     end: nextMonth,
//     allDay: true,
//     extendedProps: {
//       calendar: 'Business'
//     }
//   },
//   {
//     id: 10,
//     url: '',
//     title: 'Monthly Checkup',
//     start: prevMonth,
//     end: prevMonth,
//     allDay: true,
//     extendedProps: {
//       calendar: 'Personal'
//     }
//   }
// ];
