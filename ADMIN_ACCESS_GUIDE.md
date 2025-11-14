# 👨‍💼 Admin Login Guide - Drive Easy

## 🎯 How to Login as Admin

There are **TWO ways** to access admin features in Drive Easy:

---

## Method 1: Django Admin Interface (Recommended for Admins)

### Access Django Admin
```
URL: http://localhost:8000/admin
or
URL: http://yourdomain.com/admin
```

### Step-by-Step Instructions

#### Step 1: Go to Admin URL
```
1. Open your browser
2. Go to: http://localhost:8000/admin
3. You should see the Django Admin login page
```

#### Step 2: Login with Superuser Credentials
```
Username: admin
Password: admin123
(or your custom superuser credentials)
```

#### Step 3: Access Admin Dashboard
```
After login, you'll see:
├─ Users
├─ Customers
├─ Bookings
├─ Cars
├─ Drivers
├─ Maintenance
└─ Other models
```

---

## Method 2: Application Staff Dashboard

### Access Staff Dashboard in App
```
URL: http://localhost:8000/staff/admin-dashboard/
```

### Requirements
```
✅ Must be logged in to the app
✅ Must be marked as "staff" user
✅ Must have superuser permissions
```

### How to Access
```
1. Register/Login as a user
2. Admin makes you a staff member (in Django admin)
3. Go to: /staff/admin-dashboard/
4. See admin dashboard with statistics
```

---

## 🔧 Creating Admin Users

### If You Don't Have Admin Credentials

#### Option 1: Create Superuser via Terminal
```bash
python manage.py createsuperuser
```

**Then answer the prompts:**
```
Username: admin
Email: admin@example.com
Password: [enter password]
Password (again): [confirm]
```

**Then login with those credentials** ✅

#### Option 2: Create Staff User via Django Admin
```
1. Login to Django admin (/admin)
2. Go to "Users"
3. Click "Add User"
4. Create new user
5. Check "Staff status" checkbox
6. Check "Superuser status" checkbox
7. Click Save
```

---

## 📊 What You Can Do As Admin

### In Django Admin (/admin)
```
✅ Manage Users
   ├─ Create/edit/delete users
   ├─ Change passwords
   ├─ Set permissions
   └─ Mark as staff

✅ Manage Customers
   ├─ View customer profiles
   ├─ Edit customer details
   ├─ View aadhar/license info
   └─ Manage profile pictures

✅ Manage Bookings
   ├─ View all bookings
   ├─ Edit booking details
   ├─ Mark as returned
   ├─ Add damage fees
   └─ View cancellations

✅ Manage Cars
   ├─ Add/edit/delete cars
   ├─ Update prices
   ├─ Manage inventory
   ├─ Upload images
   └─ Set availability

✅ Manage Drivers
   ├─ Add/edit drivers
   ├─ View licenses
   ├─ Set status
   └─ Manage assignments

✅ View Maintenance
   ├─ Track maintenance records
   ├─ Manage costs
   ├─ Plan schedules
   └─ View history
```

### In Staff Dashboard (/staff/admin-dashboard/)
```
✅ View Statistics
   ├─ Total bookings
   ├─ Total revenue
   ├─ Total drivers
   ├─ Total cars
   ├─ Returned cars
   └─ Pending bookings

✅ Manage Bookings
   ├─ View all bookings
   ├─ Mark cars as returned
   ├─ View booking details
   └─ Handle damage reports

✅ View Returned Cars
   ├─ All returned bookings
   ├─ Filter by status
   ├─ View payments
   └─ Manage refunds
```

---

## 🔐 Security Notes

### Admin Access
```
⚠️ IMPORTANT:
├─ Never share admin credentials
├─ Change default password immediately
├─ Use strong passwords
├─ Use unique usernames
└─ Limit admin access to trusted staff
```

### Best Practices
```
✅ DO:
   ├─ Create individual admin accounts per person
   ├─ Change passwords regularly
   ├─ Monitor admin actions
   ├─ Use strong passwords (8+ characters, mixed)
   └─ Keep Django up to date

❌ DON'T:
   ├─ Share admin credentials
   ├─ Use "admin" as password
   ├─ Give admin access to all users
   ├─ Leave admin logged in
   └─ Use easy passwords
```

---

## 🆘 Troubleshooting

### "Admin page not found" (404 error)
```
Solution:
1. Check URL is correct: http://localhost:8000/admin
2. Make sure Django is running: python manage.py runserver
3. Check /admin is in urls (it should be by default)
```

### "Wrong username or password"
```
Solution:
1. Check username spelling
2. Check password (case-sensitive)
3. Try creating new superuser:
   python manage.py createsuperuser
```

### "Permission denied" error
```
Solution:
1. User must be marked as "staff"
2. User must be "superuser"
3. Logout and login again
4. Clear browser cache: Ctrl+Shift+Delete
```

### "Can't see staff dashboard"
```
Solution:
1. Login to main app first: /login
2. Go to /staff/admin-dashboard/
3. Must be staff member + superuser
4. Check user permissions in Django admin
```

### "Database locked" error
```
Solution:
1. Stop all running processes
2. Delete db.sqlite3.lock (if exists)
3. Restart Django: python manage.py runserver
4. Try again
```

---

## 📋 Admin Checklist

### First Time Setup
```
☑ Create superuser account
  Command: python manage.py createsuperuser

☑ Login to /admin
  URL: http://localhost:8000/admin

☑ Verify everything works
  ├─ Create test user
  ├─ Create test car
  └─ View bookings

☑ Set up staff users
  ├─ Go to Users
  ├─ Create staff members
  ├─ Mark as "Staff" and "Superuser"
  └─ Give them credentials

☑ Populate initial data
  ├─ Add cars to system
  ├─ Add drivers
  └─ Configure prices

☑ Test staff features
  ├─ Go to /staff/admin-dashboard/
  ├─ View statistics
  └─ Try marking cars as returned

☑ Configure security
  ├─ Change SECRET_KEY (production)
  ├─ Set DEBUG = False (production)
  ├─ Configure ALLOWED_HOSTS (production)
  └─ Use HTTPS (production)
```

---

## 🚀 Quick Start Commands

### Start Server
```bash
python manage.py runserver
```

### Create Admin User
```bash
python manage.py createsuperuser
```

### Access Admin
```
1. Go to: http://localhost:8000/admin
2. Login with superuser credentials
3. Done! ✅
```

### Access Staff Dashboard
```
1. Go to: http://localhost:8000/staff/admin-dashboard/
2. Must be logged in + staff member
3. Done! ✅
```

---

## 📊 Admin Interface Overview

### Users Section
```
View/Edit:
├─ Username
├─ Email
├─ First name & Last name
├─ Staff status
├─ Superuser status
├─ Active status
├─ Password
└─ Groups & Permissions
```

### Cars Section
```
View/Edit:
├─ Category
├─ AC Type
├─ Total Cars (inventory)
├─ Registration Number
├─ Image
├─ Price (daily)
├─ Price per hour
├─ Price per km
├─ Fuel consumption
├─ Status (available/repair)
└─ Damage tracking
```

### Bookings Section
```
View/Edit:
├─ Customer
├─ Car
├─ Start date/time
├─ Expected return
├─ Pickup location
├─ Drop location
├─ Advance payment
├─ Total amount
├─ Pending payment
├─ Is returned status
├─ Damage reported
├─ Damage fee
└─ Notes
```

### Drivers Section
```
View/Edit:
├─ Name
├─ License number
├─ Aadhar number
├─ Phone
├─ Email
├─ Address
├─ Years of experience
├─ Status (available/assigned/on leave)
├─ Photo
└─ Availability
```

---

## 🔑 Default Credentials (Development Only)

```
⚠️ IMPORTANT: Change these immediately in production!

Default Admin:
├─ Username: admin
├─ Password: admin123
└─ (Create your own superuser for security)

Development URL:
├─ Admin: http://localhost:8000/admin
├─ Staff Dashboard: http://localhost:8000/staff/admin-dashboard/
└─ Main App: http://localhost:8000/
```

---

## 📞 Common Admin Tasks

### Add a New Car
```
1. Go to: /admin/app/car/
2. Click "Add Car"
3. Fill in details:
   ├─ Category
   ├─ AC Type
   ├─ Registration
   ├─ Image
   ├─ Price
   ├─ Availability
   └─ Other details
4. Click Save ✅
```

### Create Staff Member
```
1. Go to: /admin/auth/user/
2. Click "Add User"
3. Fill in:
   ├─ Username
   ├─ Password (set strong password)
   └─ Confirm password
4. Click Save
5. Check boxes:
   ├─ Staff status ✓
   └─ Superuser status ✓
6. Click Save again ✅
```

### View All Bookings
```
1. Go to: /admin/app/booking/
2. See all bookings
3. Click to edit
4. Can mark as returned
5. Can add damage fees
6. Click Save ✅
```

### Mark Car as Returned (from Staff Dashboard)
```
1. Go to: /staff/admin-dashboard/
2. In pending bookings
3. Click "Mark as Returned"
4. Enter damage fee if applicable
5. Submit ✅
```

---

## ✅ Security Checklist

### Before Going to Production
```
☑ Change default admin password
☑ Create unique superuser accounts
☑ Set DEBUG = False
☑ Change SECRET_KEY
☑ Configure ALLOWED_HOSTS
☑ Use HTTPS (secure connection)
☑ Backup database regularly
☑ Monitor admin logs
☑ Restrict admin access to trusted staff
☑ Update Django to latest version
```

---

## 📊 Admin Permissions

### Types of Users

#### Superuser
```
✅ Access to everything
✅ Can manage all users
✅ Can manage all content
✅ Can access Django admin
✅ Full control
```

#### Staff User
```
✅ Can access staff dashboard
✅ Can view bookings
✅ Can mark cars as returned
✅ Limited access
✅ Cannot manage users
```

#### Regular User
```
✅ Can make bookings
✅ Can view own bookings
✅ Can cancel own bookings
✅ Cannot access admin
✅ Limited to own data
```

---

## 🎓 Learning Resources

### For Admin Users
1. Django Admin Documentation
2. This guide (START WITH THIS)
3. Staff dashboard features
4. Try basic operations first

### For Developers
1. See `ADMIN_ACCESS_GUIDE.md` (this file)
2. Check `app/admin.py` for customization
3. Review Django admin documentation
4. Explore Django permission system

---

## 🆘 Need More Help?

### Common Questions

**Q: How do I reset the admin password?**
```
A: Create new superuser:
   python manage.py createsuperuser
```

**Q: Can I give admin access to specific features only?**
```
A: Yes, via Django permission system in /admin
```

**Q: How do I backup the admin data?**
```
A: Backup database file:
   db.sqlite3 (or your database)
```

**Q: Is admin accessible from mobile?**
```
A: Yes, /admin works on mobile browsers
```

**Q: Can I customize the admin interface?**
```
A: Yes, edit app/admin.py for customization
```

---

## 🚀 Next Steps

1. **Create superuser**: `python manage.py createsuperuser`
2. **Start server**: `python manage.py runserver`
3. **Go to admin**: `http://localhost:8000/admin`
4. **Login with credentials**: Username & password you created
5. **Explore the interface**: Try adding a car or user
6. **Test staff dashboard**: `/staff/admin-dashboard/`
7. **You're done!** ✅

---

## 📝 Summary

```
QUICK REFERENCE:

Admin URL:             http://localhost:8000/admin
Staff Dashboard:       http://localhost:8000/staff/admin-dashboard/
Create Admin:          python manage.py createsuperuser
Default User:          admin (change immediately!)
Default Password:      admin123 (change immediately!)

Features:
├─ Manage users
├─ Manage bookings
├─ Manage cars
├─ Manage drivers
├─ View statistics
└─ Track operations
```

---

**Status**: ✅ Ready for Admin Use  
**Version**: 1.0  
**Last Updated**: November 13, 2025

**You're all set! Start managing your Drive Easy platform!** 🎉

