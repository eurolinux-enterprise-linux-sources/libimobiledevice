/* 
 * afc.h
 * Defines and structs and the like for the built-in AFC client
 * 
 * Copyright (c) 2008 Zach C. All Rights Reserved.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 * 
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA 
 */

#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <glib.h>
#include <stdint.h>

#include "libimobiledevice/afc.h"

#define AFC_MAGIC "CFA6LPAA"
#define AFC_MAGIC_LEN (8)

typedef struct {
	char magic[AFC_MAGIC_LEN];
	uint64_t entire_length, this_length, packet_num, operation;
} AFCPacket;

#define AFCPacket_to_LE(x) \
 	(x)->entire_length = GUINT64_TO_LE((x)->entire_length); \
	(x)->this_length   = GUINT64_TO_LE((x)->this_length); \
	(x)->packet_num    = GUINT64_TO_LE((x)->packet_num); \
	(x)->operation     = GUINT64_TO_LE((x)->operation);

#define AFCPacket_from_LE(x) \
	(x)->entire_length = GUINT64_FROM_LE((x)->entire_length); \
	(x)->this_length   = GUINT64_FROM_LE((x)->this_length); \
	(x)->packet_num    = GUINT64_FROM_LE((x)->packet_num); \
	(x)->operation     = GUINT64_FROM_LE((x)->operation);

typedef struct {
	uint64_t filehandle, size;
} AFCFilePacket;

typedef struct __AFCToken {
	struct __AFCToken *last, *next;
	char *token;
} AFCToken;

struct afc_client_int {
	idevice_connection_t connection;
	AFCPacket *afc_packet;
	int file_handle;
	int lock;
	GMutex *mutex;
};

/* AFC Operations */
enum {
	AFC_OP_STATUS          = 0x00000001,	// Status
	AFC_OP_DATA            = 0x00000002,	// Data
	AFC_OP_READ_DIR        = 0x00000003,	// ReadDir
	AFC_OP_READ_FILE       = 0x00000004,	// ReadFile
	AFC_OP_WRITE_FILE      = 0x00000005,	// WriteFile
	AFC_OP_WRITE_PART      = 0x00000006,	// WritePart
	AFC_OP_TRUNCATE        = 0x00000007,	// TruncateFile
	AFC_OP_REMOVE_PATH     = 0x00000008,	// RemovePath
	AFC_OP_MAKE_DIR        = 0x00000009,	// MakeDir
	AFC_OP_GET_FILE_INFO   = 0x0000000a,	// GetFileInfo
	AFC_OP_GET_DEVINFO     = 0x0000000b,	// GetDeviceInfo
	AFC_OP_WRITE_FILE_ATOM = 0x0000000c,	// WriteFileAtomic (tmp file+rename)
	AFC_OP_FILE_OPEN       = 0x0000000d,	// FileRefOpen
	AFC_OP_FILE_OPEN_RES   = 0x0000000e,	// FileRefOpenResult
	AFC_OP_READ            = 0x0000000f,	// FileRefRead
	AFC_OP_WRITE           = 0x00000010,	// FileRefWrite
	AFC_OP_FILE_SEEK       = 0x00000011,	// FileRefSeek
	AFC_OP_FILE_TELL       = 0x00000012,	// FileRefTell
	AFC_OP_FILE_TELL_RES   = 0x00000013,	// FileRefTellResult
	AFC_OP_FILE_CLOSE      = 0x00000014,	// FileRefClose
	AFC_OP_FILE_SET_SIZE   = 0x00000015,	// FileRefSetFileSize (ftruncate)
	AFC_OP_GET_CON_INFO    = 0x00000016,	// GetConnectionInfo
	AFC_OP_SET_CON_OPTIONS = 0x00000017,	// SetConnectionOptions
	AFC_OP_RENAME_PATH     = 0x00000018,	// RenamePath
	AFC_OP_SET_FS_BS       = 0x00000019,	// SetFSBlockSize (0x800000)
	AFC_OP_SET_SOCKET_BS   = 0x0000001A,	// SetSocketBlockSize (0x800000)
	AFC_OP_FILE_LOCK       = 0x0000001B,	// FileRefLock
	AFC_OP_MAKE_LINK       = 0x0000001C,	// MakeLink
	AFC_OP_SET_FILE_TIME   = 0x0000001E	// set st_mtime
};

