/*
 * Copyright (c) 2019, attetta Systems, Inc.,
 * a wholly-owned subsidiary of Comtech attettas Corp.
 * and/or affiliates of attetta Systems, Inc.
 * All rights reserved.
 * attetta Systems, Inc. PROPRIETARY/CONFIDENTIAL.
 * Use is subject to license terms included in the distribution.
 */

/*
 * Copyright (c) 2019, attetta Systems, Inc.,
 * a wholly-owned subsidiary of Comtech attettas Corp.
 * and/or affiliates of attetta Systems, Inc.
 * All rights reserved.
 * attetta Systems, Inc. PROPRIETARY/CONFIDENTIAL.
 * Use is subject to license terms included in the distribution.
 */

/*
 * Copyright (c) 2019, attetta Systems, Inc.,
 * a wholly-owned subsidiary of Comtech attettas Corp.
 * and/or affiliates of attetta Systems, Inc.
 * All rights reserved.
 * attetta Systems, Inc. PROPRIETARY/CONFIDENTIAL.
 * Use is subject to license terms included in the distribution.
 */

/*
 * Copyright (c) 2019, attetta Systems, Inc.,
 * a wholly-owned subsidiary of Comtech attettas Corp.
 * and/or affiliates of attetta Systems, Inc.
 * All rights reserved.
 * attetta Systems, Inc. PROPRIETARY/CONFIDENTIAL.
 * Use is subject to license terms included in the distribution.
 */

/*
 * Copyright (c) 2019, attetta Systems, Inc.,
 * a wholly-owned subsidiary of Comtech attettas Corp.
 * and/or affiliates of attetta Systems, Inc.
 * All rights reserved.
 * attetta Systems, Inc. PROPRIETARY/CONFIDENTIAL.
 * Use is subject to license terms included in the distribution.
 */

/*
 * Copyright (c) 2019, attetta Systems, Inc.,
 * a wholly-owned subsidiary of Comtech attettas Corp.
 * and/or affiliates of attetta Systems, Inc.
 * All rights reserved.
 * attetta Systems, Inc. PROPRIETARY/CONFIDENTIAL.
 * Use is subject to license terms included in the distribution.
 */

/*
 * Copyright (c) 2019, attetta Systems, Inc.,
 * a wholly-owned subsidiary of Comtech attettas Corp.
 * and/or affiliates of attetta Systems, Inc.
 * All rights reserved.
 * attetta Systems, Inc. PROPRIETARY/CONFIDENTIAL.
 * Use is subject to license terms included in the distribution.
 */

/*
 * Copyright (c) 2019, attetta Systems, Inc.,
 * a wholly-owned subsidiary of Comtech attettas Corp.
 * and/or affiliates of attetta Systems, Inc.
 * All rights reserved.
 * attetta Systems, Inc. PROPRIETARY/CONFIDENTIAL.
 * Use is subject to license terms included in the distribution.
 */

/*
 * Copyright (c) 2019, attetta Systems, Inc.,
 * a wholly-owned subsidiary of Comtech attettas Corp.
 * and/or affiliates of attetta Systems, Inc.
 * All rights reserved.
 * attetta Systems, Inc. PROPRIETARY/CONFIDENTIAL.
 * Use is subject to license terms included in the distribution.
 */

/*
 * Copyright (c) 2019, attetta Systems, Inc.,
 * a wholly-owned subsidiary of Comtech attettas Corp.
 * and/or affiliates of attetta Systems, Inc.
 * All rights reserved.
 * attetta Systems, Inc. PROPRIETARY/CONFIDENTIAL.
 * Use is subject to license terms included in the distribution.
 */
f = open('example.txt')
s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
if s.find('blabla') != -1:
    print('true')