# 🔐 Admin Login - Quick Reference Card

## ⚡ Quickest Way to Login as Admin

### 3 Simple Steps:

```
1️⃣  START SERVER
    python manage.py runserver

2️⃣  GO TO ADMIN
    http://localhost:8000/admin

3️⃣  LOGIN
    Username: admin
    Password: admin123
```

**That's it! ✅**

---

## 🔑 Admin Credentials (Development)

```
URL:      http://localhost:8000/admin
Username: admin
Password: admin123
```

⚠️ **Change these in production!**

---

## 📍 Two Ways to Access Admin

### Way 1: Django Admin (Recommended)
```
URL: http://localhost:8000/admin
├─ Full control
├─ Manage all data
├─ Best for advanced control
└─ Requires superuser
```

### Way 2: Staff Dashboard
```
URL: http://localhost:8000/staff/admin-dashboard/
├─ View statistics
├─ Manage bookings
├─ Mark cars returned
└─ Requires staff + superuser
```

---

## 🚀 If You Don't Have Admin Credentials

### Create New Admin User:
```bash
python manage.py createsuperuser
```

Then answer:
- Username: [your username]
- Email: [your email]
- Password: [strong password]

Then login! ✅

---

## ✅ What You Can Do As Admin

```
✅ Manage Users          → Add/edit/delete users
✅ Manage Cars           → Add/edit/delete cars
✅ Manage Bookings       → View/edit/mark returned
✅ Manage Drivers        → Add/edit drivers
✅ View Statistics       → Dashboard with metrics
✅ Set Permissions       → Control user access
✅ Manage Inventory      → Update car availability
✅ Track Maintenance     → Maintenance records
```

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "404 Not Found" | Make sure server running: `python manage.py runserver` |
| "Wrong password" | Create new admin: `python manage.py createsuperuser` |
| "Permission denied" | User must be superuser (check in /admin/auth/user/) |
| "Page won't load" | Check URL is exactly: `http://localhost:8000/admin` |

---

## 📱 Mobile Access

✅ Admin works on mobile!
```
URL: http://localhost:8000/admin
(Access from any device on same network)
```

---

## 🔒 Security Reminders

```
⚠️ DO:
✅ Change password immediately (don't use admin123)
✅ Never share credentials
✅ Create individual accounts per person
✅ Use strong passwords (8+ characters)

⚠️ DON'T:
❌ Share admin login
❌ Use weak passwords
❌ Leave admin logged in
❌ Use default credentials in production
```

---

## 🎯 Common Tasks

### Add a Car
```
1. Go to /admin
2. Click "Cars"
3. Click "Add Car"
4. Fill details
5. Click Save ✅
```

### Create Staff Member
```
1. Go to /admin
2. Click "Users"
3. Click "Add User"
4. Check "Staff" & "Superuser"
5. Click Save ✅
```

### View All Bookings
```
1. Go to /admin
2. Click "Bookings"
3. See all bookings
4. Click to edit ✅
```

### Check Statistics
```
1. Go to /staff/admin-dashboard/
2. View total bookings
3. View revenue
4. See pending bookings ✅
```

---

## 🚀 Start Here!

```
STEP 1: python manage.py runserver
STEP 2: http://localhost:8000/admin
STEP 3: admin / admin123
STEP 4: You're in! 🎉
```

---

**Full Guide**: See `ADMIN_ACCESS_GUIDE.md` for complete details  
**Status**: ✅ Ready to Use

