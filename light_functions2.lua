
-- ##########################################
--    FUNKTIONER ATT ANVÄNDA I TESTSCRIPT
-- ##########################################

print("light_functions2.lua korrekt inläst.")

local lights = {}

function lights.timestamp()

	time = os.date("%H:%m")

	timestamp = time
	extension = ".txt"
	filename = string.format("C:\\TestWizard\\Scripts\\Log\\testlogg__%s%s",timestamp, extension)

	return time
end

-- ##########################################

function lights.on_off()


    --Ok, ErrorCode = LoadReferenceBitmap("warmest2.bmp")
    Ok, ErrorCode, Message = Camera.InitializeNetwork()

	Time, Similarity, Position, ErrorCode = WaitForPattern("light_on3.bmp", 80, 10, 1, 0, 0, 1920, 1080)
	
    return Similarity
end


-- ##########################################
 
function lights.max_brightness_coldest()

    Ok, ErrorCode = LoadReferenceBitmap("coldest2.bmp")
    Time, Similarity, Color, ErrorCode = WaitForColor(835, 478, 213, 112, 0xFEFCF9, 0x0A0A0A, 50, 10)
	
    return Similarity
end
-- ##########################################

function lights.max_brightness_cold()
	
    Ok, ErrorCode = LoadReferenceBitmap("cold2.bmp")
	Time, Similarity, Color, ErrorCode = WaitForColor(835, 478, 213, 112, 0xFEEBDA, 0x0A0A0A, 50, 10)
   
   return Similarity
end



-- ############################################

function lights.max_brightness_warm()
	
    Ok, ErrorCode = LoadReferenceBitmap("warm2.bmp")
	Time, Similarity, Color, ErrorCode = WaitForColor(835, 478, 213, 112, 0xFFEAC7, 0x0A0A0A, 50, 10)
    
    return Similarity
end

-- ############################################

function lights.max_brightness_warmest()


    Ok, ErrorCode = LoadReferenceBitmap("warmest2.bmp")
	Time, Similarity, Color, ErrorCode = WaitForColor(835, 478, 213, 112, 0xFFD9A1, 0x0A0A0A, 50, 10)
	
	
    return Similarity
end


-- ############################################

function lights.brightness_level_254()

    Ok, ErrorCode = LoadReferenceBitmap("coldest_brightness_254.bmp")
	Time, Similarity, Color, ErrorCode = WaitForColor(835, 478, 213, 112, 0xFEFAF6, 0x0A0A0A, 50, 10)

    return Similarity
end

--############################################

function lights.brightness_level_190()

    Ok, ErrorCode = LoadReferenceBitmap("coldest_brightness_190.bmp")
    Time, Similarity, Color, ErrorCode = WaitForColor(835, 478, 213, 112, 0xF8EBEB, 0x0A0A0A, 50, 10)
    return Similarity
end


--###########################################

function lights.brightness_level_125()

    Ok, ErrorCode = LoadReferenceBitmap("coldest_brightness_125.bmp")
    Time, Similarity, Color, ErrorCode = WaitForColor(835, 478, 213, 112, 0xAC9FA2, 0x0A0A0A, 50, 10)
    return Similarity
end


--###########################################

function lights.brightness_level_65()

    Ok, ErrorCode = LoadReferenceBitmap("coldest_brightness_65.bmp")
	Time, Similarity, Color, ErrorCode = WaitForColor(835, 478, 213, 112, 0x6E6368, 0x0A0A0A, 50, 10)
    return Similarity
end


return lights
