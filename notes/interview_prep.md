# Interview Preparation Guide

Comprehensive guide for backend engineering interviews.

## 🎯 Python Interview Topics

### Core Python (Beginner Level)

**Common Questions**:

1. What are Python data types?
   - Answer: int, float, string, bool, list, tuple, dict, set
2. What's the difference between list and tuple?
   - Answer: Lists are mutable, tuples are immutable
3. How do you reverse a list?
   - Answer: `list[::-1]` or `list.reverse()`
4. What's the difference between == and is?
   - Answer: == checks value, is checks identity

### Functions & OOP (Intermediate)

1. What are decorators and how do they work?
2. Explain \*args and \*\*kwargs
3. What is the difference between instance and class variables?
4. How does inheritance work in Python?
5. What are dunder methods?

### Advanced Python

1. How do generators and iterators work?
2. What is a context manager?
3. Explain async/await
4. What's the difference between deep and shallow copy?
5. How does the GIL affect multithreading?

---

## 🌐 Backend Interview Topics

### HTTP & REST

1. What HTTP methods do you know?
   - GET: Retrieve data
   - POST: Create data
   - PUT: Update entire resource
   - PATCH: Partial update
   - DELETE: Remove data

2. What are HTTP status codes?
   - 200: OK (success)
   - 201: Created
   - 400: Bad Request
   - 401: Unauthorized
   - 403: Forbidden
   - 404: Not Found
   - 500: Server Error

3. What is REST?
   - Representational State Transfer
   - Uses HTTP methods
   - Stateless architecture
   - Resource-based URIs

### Databases

**SQL Questions**:

1. Explain the different types of JOINs
2. What are indexes and why use them?
3. What is normalization?
4. Explain ACID properties
5. What's the difference between SQL and NoSQL?

**Example Answer - JOINs**:

```sql
INNER JOIN - Only matching records
LEFT JOIN - All from left table + matches
RIGHT JOIN - All from right table + matches
FULL OUTER JOIN - All from both tables
```

---

## 💡 Common Backend Interview Questions

### Architecture Questions

1. **How would you design a URL shortener?**
   - Database schema
   - API endpoints
   - Caching strategy
   - Scalability concerns

2. **How would you design a social media feed?**
   - Data model
   - How to fetch efficiently
   - Caching strategy
   - Real-time updates

3. **How would you handle 1 million requests per day?**
   - Caching
   - Database optimization
   - Load balancing
   - Message queues

### Security Questions

1. How do you store passwords?
   - Use bcrypt or similar hashing
   - Never store plain text
   - Use salt

2. How does authentication work?
   - User login with credentials
   - Server creates JWT token
   - Client sends token with requests
   - Server validates token

3. What's CORS and why is it important?
   - Cross-Origin Resource Sharing
   - Security mechanism
   - Prevents unauthorized cross-site requests

### Performance Questions

1. How do you optimize database queries?
   - Indexes
   - Query optimization
   - Denormalization when needed
   - Connection pooling

2. How would you cache data?
   - Cache frequently accessed data
   - Use Redis
   - Implement cache invalidation strategy

3. How do you handle high traffic?
   - Horizontal scaling
   - Load balancing
   - Caching
   - Database optimization

---

## 🎯 Interview Prep Checklist

### Before Interview

- [ ] Review core Python concepts
- [ ] Practice coding problems
- [ ] Understand system design basics
- [ ] Know your projects well
- [ ] Prepare questions to ask
- [ ] Get good sleep night before

### During Interview

- [ ] Listen carefully to questions
- [ ] Think before coding
- [ ] Write clean code
- [ ] Explain your approach
- [ ] Ask clarifying questions
- [ ] Test your code

### Technical Interview Tips

1. **Clarify the problem**
   - Ask questions about requirements
   - Confirm edge cases
   - Understand constraints

2. **Think out loud**
   - Explain your approach
   - Show your reasoning
   - Consider trade-offs

3. **Write clean code**
   - Use meaningful variable names
   - Add comments
   - Follow style guides
   - Handle errors

4. **Test your solution**
   - Try edge cases
   - Verify the logic
   - Check for bugs

---

## 📚 Sample Interview Problems

### Problem 1: Reverse a String

```python
def reverse_string(s):
    return s[::-1]

# Test
print(reverse_string("Hello"))  # "olleH"
```

### Problem 2: Find Two Sum

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test
print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

### Problem 3: Longest Common Prefix

```python
def longest_common_prefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]

    return strs[0]

# Test
print(longest_common_prefix(["flower","flow","flight"]))  # "fl"
```

---

## 🎤 Behavioral Questions

### Common Behavioral Questions

1. **Tell me about yourself**
   - Background
   - Relevant experience
   - Learning journey
   - Career goals

2. **Describe a challenging problem you solved**
   - Situation
   - Challenge
   - Action
   - Result

3. **How do you handle disagreements?**
   - Listen to others
   - Explain your perspective
   - Find compromise
   - Respect decisions

4. **What's your biggest weakness?**
   - Be honest
   - Show you're working on it
   - Frame positively

5. **Why do you want this job?**
   - Research the company
   - Align with values
   - Show genuine interest

### STAR Method for Behavioral Questions

- **S**ituation: Set the context
- **T**ask: Explain what you needed to do
- **A**ction: Describe what you did
- **R**esult: Share the outcome

**Example**:

> "In my previous project (S), we needed to optimize a slow database query (T). I analyzed the query execution plan and added an index on the frequently searched column (A). This reduced query time from 5 seconds to 200ms (R)."

---

## 🔄 Mock Interview Checklist

### Before Mock Interview

- [ ] Choose relevant problem
- [ ] Set time limit (45 minutes)
- [ ] Use actual coding environment
- [ ] Have pen/paper ready
- [ ] Practice thinking out loud

### During Mock Interview

- [ ] Clarify problem (5 min)
- [ ] Discuss approach (10 min)
- [ ] Code solution (20 min)
- [ ] Test and optimize (10 min)

### After Mock Interview

- [ ] Review what went well
- [ ] Identify areas to improve
- [ ] Practice weak areas
- [ ] Repeat process

---

## 📈 Interview Progress Tracker

### Technical Skills Assessment

- [ ] Core Python: 8/10
- [ ] Data Structures: 7/10
- [ ] Algorithms: 6/10
- [ ] System Design: 5/10
- [ ] Databases: 6/10
- [ ] API Design: 7/10

### Areas to Improve

1. ***
2. ***
3. ***

---

## 🚀 Final Tips

### Do's ✅

- ✅ Practice coding daily
- ✅ Study system design
- ✅ Mock interview with friends
- ✅ Review your projects thoroughly
- ✅ Learn from failed interviews
- ✅ Stay confident

### Don'ts ❌

- ❌ Memorize solutions
- ❌ Skip problem understanding
- ❌ Write messy code
- ❌ Ignore test cases
- ❌ Give up easily
- ❌ Be arrogant

---

## 📞 Resources

- LeetCode: https://leetcode.com/
- HackerRank: https://www.hackerrank.com/
- Interviewing.io: https://interviewing.io/
- System Design Primer: https://github.com/donnemartin/system-design-primer

---

**Remember**: Interviews test problem-solving, not memorization. Think clearly, communicate well, and code confidently! 💪

**Last Updated**: May 13, 2024
