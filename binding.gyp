{
	'targets' : [
		{
			'target_name': 'scrypt_lib',
			'type': 'static_library',
			'defines': [ #This config file is custom generated for each POSIX OS
				'CONFIG_H_FILE="../config.h"',
			],
			'include_dirs' : [
				'scrypt-1.1.6',
				'scrypt-1.1.6/lib/util',
				'scrypt-1.1.6/lib/crypto',
				'scrypt-1.1.6/lib/scryptenc',
			],
			'sources': [
				'scrypt-1.1.6/lib/crypto/crypto_scrypt-sse.c',
				'scrypt-1.1.6/lib/crypto/sha256.c',
				'win/mman.c'
			],
			'conditions': [
				[
					'OS == "win"', { 
						#'msvs_settings' : {
						#	'VCCLCompilerTool' : {
						#		'AdditionalOptions' : ['/TC']
						#	}
						#},
						'libraries': [
							'-lC:/OpenSSL-Win32/lib/libeay32.lib',
						],
						'include_dirs': [
							'win/include',
							'C:/OpenSSL-Win32/include',
						],
					},
				]
			],
		},
	],
}
